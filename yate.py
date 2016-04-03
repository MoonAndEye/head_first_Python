
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')


def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text) 
    """
    這裡,在header把 templates/header.html讀出來
    然後再把header換掉, the_title是你想要的東西, title是原來的?
    """
    return(header.substitute(title=the_title))

"""

"""

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    """
    要先把link_string設為空，讓python知道現在要處理string
    一開始開啟的檔 templates/footer.html
    裡面可能有很多超連結
    然後最後把原來的link換掉
    """
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))
"""
這是footer, 不太確定這個是不是一定要加的
看結構可能是一個 dict

"""
def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 
