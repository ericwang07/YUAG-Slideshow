from flask import Flask, request, make_response, redirect, url_for, render_template
from database import search
from time import localtime, asctime, strftime

# APPLICATION TIER - MAIN CODE
# - Includes Routes that generate responses

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():                    
    html = render_template('index.html')            
    response = make_response(html)
    return response

# Called by ajax request in getResults of index.html
@app.route('/searchresults', methods=['GET'])
def search_results():    
    rows = search() # random search - no args    
    print("successfully searched")
    
    html = ""
    
    image_html = '''
    <img src=https://media.collections.yale.edu/thumbnail/yuag/obj/%s alt="%s, %s" onerror='handleNoImage(this);'></img>
    '''
    html += image_html % (rows[3], rows[0], rows[1])
    
    headers_html = '''
    <h2>%s</h2>
    <h3>%s</h3>
    <ul>
    '''
    headers_html = headers_html % rows[:2]
    html += headers_html
        
    if rows[2]:
        agents_group = rows[2]
        agents = agents_group.split(",")
        
        pattern = '''
            <li>%s</li>
        '''
        
        for agent in agents:
            html += pattern % agent
        # html += pattern % rows[2]
            
        html += '''
        </ul>
        '''
    
    response = make_response(html)
    print("generated response")
    # Sends HTML response to handleResponse in index.html.    
    return response
        
    
    
