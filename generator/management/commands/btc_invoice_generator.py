from django.core.management.base import BaseCommand, CommandError
from generator.models import *


import struct
import sys
import os
import time
import datetime
import string
import random
import subprocess
import shutil
import tempfile 
from pprint import *

#   TODO: 
#   Retry handler
#   Make an API

class Command(BaseCommand):
    help = 'Generates invoices for the customers of bitvivo.co.uk'
    debug_level = 1 
    
    #
    # Set encoding to utf-8
    #

    reload(sys)
    sys.setdefaultencoding("utf-8")

    # Write out some text message
    def say(self, txt):
        return self.stdout.write("[%s] btc_ivoice_generator/btc_ivoice_generator: %s" % (time.ctime(), txt) )

    #
    # Write out a debug message 
    # (if debug level is appropriate)
    #

    def debug(self, txt_debug_level, txt):
        if self.debug_level >= txt_debug_level:
            return self.say(txt)
        else:
            return False

    def add_arguments(self, parser):
        parser.add_argument('debug_level', nargs='+', type=int)

    #
    # Escapes special latex codes so no funny business happens.
    #

    def escape_latex(self, s):

        _latex_special_chars = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
            '\n': r'\\',
            '-': r'{-}',
            '\xA0': '~',  # Non-breaking space
        }

        return ''.join(_latex_special_chars.get(c, c) for c in s)

    def write_latex(self, file_name, latex_output):
        with open(file_name, 'w') as f:
            f.write(latex_output)

    #
    # Generates a random 15 letter string to use in generate_file_name(()
    #

    def random_15_letter_string(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in xrange(15))     

    #
    # Generates a unique file name for each invoice by the format: invoice_[unixtime]_[15 random chars].tex
    #

    def generate_file_name(self):
        return "invoice_" + str(int(time.time())) + "_" + self.random_15_letter_string()  #the timestamp is converted to int to round down and then converted to string
    
    def handle(self, *args, **options):
        self.say('Initializing ...')

        # 
        # Set debug level
        #

        try:
            self.debug_level = options['debug_level'][0]

        except:
            self.debug_level = 1

        self.debug(1, "Set debug level; debug_level=%i" % self.debug_level)
        
        #Here will be some initilizing code.

        self.say('...initialized. Started processing.')

        while True:
            invoice_requests = Invoice.objects.filter(closed=False)

            for invoice_request in invoice_requests:

                #
                # Get the data and generate the output string to write out to temp.tex 
                #

                latex_output = ("\\newcommand{\\firstname}{%s}" % self.escape_latex(str(invoice_request.first_name)) + "\n" + 
                                "\\newcommand{\\lastname}{%s}" % self.escape_latex(str(invoice_request.last_name)) + "\n" +
                                "\\newcommand{\\address}{%s}" % self.escape_latex(str(invoice_request.address)) + "\n" +
                                "\\newcommand{\\country}{%s}" % self.escape_latex(str(invoice_request.country)) + "\n" +
                                "\\newcommand{\\email}{%s}" % self.escape_latex(str(invoice_request.email)) + "\n" +
                                "\\newcommand{\\currency}{%s}" % self.escape_latex(str(invoice_request.currency)) + "\n" + 
                                "\\newcommand{\\invoicedate}{%s}" % self.escape_latex(str(invoice_request.date)) + "\n" + #'\date' is reserved in LaTeX, using 
                                "\\newcommand{\\invoicenr}{%s}" % self.escape_latex(str(invoice_request.pk)))             # \invoicedate instead.
                #
                # Add the items.
                #

                for index in xrange(len(invoice_request.items.all())):
                    latex_output += "\\expandafter\\newcommand\\csname item%s\\endcsname{%s}" % (str(index), self.escape_latex(str(invoice_request.items.all()[index]))) + "\n"

                #
                # Generating the filenames.
                #

                template_file_name = "invoice_template.tex"
                stripped_file_name = self.generate_file_name()
                tex_file_name = stripped_file_name + ".tex"
                pdf_file_name = stripped_file_name + ".pdf"

                #
                # Writing out temp files to a temp dir. temp.tex contain the information about each invoice. 
                # This is then included into the template before compiling. After the file we want is generated
                # it is copied the right place and the temp directory deleted.
                #

                temp_dir = tempfile.mkdtemp()

                try:   
                    temp_file_name = temp_dir + "/" + "temp.tex"
                    self.debug(3, "Writing out data to %s" % temp_file_name)
                    self.write_latex(temp_file_name, latex_output)

                    #
                    # Generating the invoice in pdf.
                    #

                    current_dir = os.getcwd()
                    os.symlink(current_dir + "/" + template_file_name, temp_dir + "/" + tex_file_name)
                    os.chdir(temp_dir) #we move to the temporary directory we made to generate the .pdf file there.

                    self.debug(3, "Generating invoice as %s" % pdf_file_name)

                    try:
                        pdflatex_output = subprocess.check_output(['xelatex', '-halt-on-error', '-interaction=nonstopmode', temp_dir + "/" + tex_file_name])
                        invoice_request.success = True
                        self.debug(2, "Invoice generated as %s" % pdf_file_name)
                    except subprocess.CalledProcessError as error:
                        invoice_request.success = False
                        self.debug(3, "ERROR: No output PDF file produced!")

                    #
                    # Copy the result to wherever we want it. The program directory for now
                    #

                    os.chdir(current_dir)

                    try:                
                        shutil.copy(temp_dir + "/" + pdf_file_name, "pdf_dump/" + pdf_file_name)
                    except (IOError, os.error):
                        self.debug(4, "ERROR: Could not copy %s. The file was probably never made by xelatex." % pdf_file_name)

                #
                # Finally remove the temporary files.
                #

                finally:
                    shutil.rmtree(temp_dir)

                #
                # Closing the request and updating the database.
                #

                invoice_request.closed = True #closing the request.
                invoice_request.save()

            time.sleep(0.150) 



