from fpdf import FPDF
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--font-size", help="Changing the Font size of the Resume", type=int, required=True)
parser.add_argument("--font-color", help="Changing the Font color of the Resume (hex format, e.g., #FF5733)", type=str, required=True)
parser.add_argument("--background-color", help="Changing the Background Color of the Resume (hex format, e.g., #ABC123)", type=str, required=True)

args = parser.parse_args()
font_size = args.font_size
font_color = args.font_color
background_color = args.background_color

font_red_color=int(font_color[1:3],16)
font_green_color=int(font_color[3:5],16)
font_blue_color=int(font_color[5:7],16)
font_colors=(font_red_color,font_green_color,font_blue_color)

bkgnd_red_color=int(background_color[1:3],16)
bkgnd_green_color=int(background_color[3:5],16)
bkgnd_blue_color=int(background_color[5:7],16)
bkgnd_colors=(bkgnd_red_color,bkgnd_green_color,bkgnd_blue_color)


my_name = 'Kodali Dinesh Siddhartha'
my_mail = '23110168@iitgn.ac.in'
my_contact='+91 9392454652'
my_github='Github'
my_linkedin='Linkedin'
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 25)
        w = self.get_string_width(my_name) + 6
        self.set_x((210 - w) / 2)
        self.set_text_color(128, 0, 128)
        self.cell(w, 9, my_name, 0, 1, 'C')

    def contact(self,start,contact,link_bool,link):
        self.set_text_color(*font_colors)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 8)
        self.set_x(start)
        self.cell(5, 10, '●') 
        self.set_font('Arial',"", font_size)
        if(link_bool):
            self.set_link(self.add_link())
            self.cell(50, 10, contact,link=link)  
        else:
            self.cell(50, 10, contact)  

    def add_line(self,x1,y1,x2,y2):
        self.set_draw_color(128, 0, 128)
        self.line(x1, y1, x2, y2)
        self.ln(2)
    
    def category(self,title):
        self.ln(6)
        self.set_font('Arial', 'B', font_size*1.2)
        self.set_text_color(128, 0, 128)
        self.cell(10, 6, title,ln=1)
        self.ln(5)
    
    def headings(self,degree,Specialization,Institute,Year,CPI):
        self.set_font('Arial', 'B', font_size)
        self.set_text_color(*font_colors)
        self.set_draw_color(0, 0, 0)
        self.cell(30, 10, degree,border=1,align='C')
        self.cell(60, 10, Specialization,border=1,align='C')
        self.cell(50, 10, Institute,border=1,align='C')
        self.cell(30, 10, Year,border=1,align='C')
        self.cell(20, 10, CPI,border=1,align='C')
        self.ln(10)
    
    def description(self,degree,Specialization,Institute,Year,CPI):
        self.set_font('Arial', '', font_size)
        self.set_text_color(*font_colors)
        self.set_draw_color(0, 0, 0)
        self.cell(30, 10, degree,border=1,align='C')
        self.cell(60, 10, Specialization,border=1)
        self.cell(50, 10, Institute,border=1)
        self.cell(30, 10, Year,border=1,align='C')
        self.cell(20, 10, CPI,border=1,align='C')
        self.ln(10)
        
    def skills(self,sub_heading,description,colon_bool):
        self.set_text_color(*font_colors)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font('DejaVu', '', 8)
        self.set_x(5)
        self.cell(5, 5, '●') 
        self.set_font('Arial',"", font_size)
        self.cell(52, 5, sub_heading) 
        if(colon_bool):
            self.cell(10, 6, ": ") 
        self.multi_cell(0, 5, description)   
        self.ln(5)
        
    def desc(self,description):
        self.set_text_color(*font_colors)
        self.set_font('DejaVu', '', font_size)
        self.set_x(30)
        self.multi_cell(0, 6, description)   
        self.ln(5)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', font_size*0.8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


pdf = PDF()
pdf.add_page()

pdf.alias_nb_pages()
pdf.set_fill_color(*bkgnd_colors)
pdf.rect(0, 0, pdf.w, pdf.h, 'F')
pdf.header()
pdf.contact(25, my_mail,1,"https://mail.google.com/mail/?view=cm&fs=1&to=23110168@iitgn.ac.in&subject=Your%20Subject&body=Your%20Message")
pdf.contact(75, my_contact,0,"")
pdf.contact(120, my_github,1,"https://github.com/DineshSiddhartha/")
pdf.contact(150, my_linkedin,1,"https://www.linkedin.com/in/dinesh-siddhartha-k-b95a54291/")
current_y = pdf.get_y() 
pdf.add_line(10,current_y+12,150,current_y+12)
pdf.ln(9)
pdf.category('EDUCATION')
pdf.headings('Degree','Specialization','Institute','Year','CPI/%')
pdf.description('B.Tech','Artificial Intelligence','IIT Gandhinagar','2023-Present','8.79/10')
pdf.description('Class XII','Physics,Chemistry,Maths','FIITJEE Junior College','2021-2023','97.9%')
pdf.description('Class X','General Education','DAV Public School','2011-2021','95.8%')
current_y = pdf.get_y() 
pdf.add_line(10, current_y+5,150,current_y+5)
pdf.category('SKILLS')
pdf.skills('Programming Languages','Python, C, C++',1)
pdf.skills('Tools','SQL,CSV',1)
pdf.skills('Web Technologies (Basics)','Flask, JavaScript, HTML, CSS',1)
pdf.skills('Libraries','NumPy, Pandas, PyTorch, TensorFlow, OpenCV',1)
pdf.skills('Others','Data Structures and Algorithms, Machine Learning, Deep Learning, NLP , Data Visualization',1)
current_y = pdf.get_y() 
pdf.add_line(10, current_y+5,150,current_y+5)
pdf.category('PROJECT EXPERIENCE')
pdf.skills('Activity Recognition Using Machine Learning',"",0)
pdf.desc('Achieved 68 percent accuracy in activity detection using real-time accelerometer data with a ML model.')
pdf.skills('Next-Word Prediction Model Using Shakespeare Dataset',"",0)
pdf.desc('Developed a next-word prediction system utilizing an MLP-based text generator trained on Shakespeare’s works.')
pdf.skills('Basic CV and NLP Tasks',"",0)
pdf.desc('Completed Deep Learning and NLP courses on Coursera, gaining hands-on experience in addressing real-world computer vision and natural language processing tasks through course assignments')


# Output the PDF
pdf.output('My_Resume.pdf', 'F')
