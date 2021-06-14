from flask import Flask, jsonify, request, render_template,abort
import re
import datetime
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
from flask_cors import CORS
import requests
from flask_restplus import Resource, Api
from werkzeug.utils import cached_property

app = Flask(__name__)
CORS(app)
api = Api(app)

pattern='[a-m]+'
pattern1='[n-z]+'
#username ='abc'
with open("coordinationprotocol.json", encoding="utf8") as file:
    data = json.load(file)
start_state = data['startstate'][0]
final_state = data['finalstate']
print(data)
api_order_list=[]
next_state=[]
print(api_order_list)

class service(Resource):
    def get(self):
        #print(data['service1']['json'])

        username = request.args.get('name')
        current_api=request.args.get('api')
        print(next_state)

        if(len(api_order_list)==0):
            print("After len")
            print(current_api)
            print(data['startstate'][0])

            if(current_api==data['startstate'][0]):

                api_order_list.append(current_api)
                if re.search(pattern, username[0]):
                    next_state.append(data[current_api]['json'])
                elif re.search(pattern1, username[0]):
                    next_state.append(data[current_api]['xml'])
                link = str('http://127.0.0.1:5003/' + current_api + '/' + username)
                resp = requests.get(link)
                return resp.text

            else:
                return "Error, please start from initial state"
        elif (next_state[len(next_state)-1]==current_api and current_api not in final_state):
            api_order_list.append(current_api)
            try:
                if re.search(pattern, username[0]):
                    next_state.append(data[current_api]['json'])
                elif re.search(pattern1, username[0]):
                    next_state.append(data[current_api]['xml'])
            except:
                next_state.append(data[current_api]['both'])
            link = str('http://127.0.0.1:5003/' + current_api + '/' + username)
            resp = requests.get(link)
            print(next_state)
            return resp.text
        elif(current_api in final_state):

            return "Final State"
        else:

            return "Error, input is not as per the co-ordination protocol"












#print(username[0])
JSON_Details={}
@app.route('/coordinationprotocol')
def signUp():
    return render_template('../templates/index.html')

class BadRequest(Exception):
    """Custom exception class to be thrown when local error occurs."""
    def __init__(self, message, status=400, payload=None):
        self.message = message
        self.status = status
        self.payload = payload


@app.errorhandler(BadRequest)

class service1(Resource):
    def get(self,username):

        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)

            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service2(Resource):
    def get(self,username):

        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service3(Resource):
    def get(self,username):

        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service4(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service5(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service6(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service7(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service8(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"
class service9(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"

class service10(Resource):
    def get(self,username):
        print("Hey I am username",username)
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+":"+str(current_time.minute)+":"+str(current_time.second)
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)

            root = ET.Element("User_Details")
            ET.SubElement(root, 'username').text = username
            ET.SubElement(root, "invocation_date").text = invocation_date
            ET.SubElement(root, "invocation_date").text = invocation_time


            tree= ET.ElementTree(root)
            new_xml = ET.tostring(root, encoding='utf8').decode('utf8')
            #print(new_xml)
            xmlnew = xml.dom.minidom.parseString(new_xml)
            xml_pretty_str = xmlnew.toprettyxml()
            return xml_pretty_str
        else:
            return "Error in your text, Text should be in between A-Z"



api.add_resource(service, '/service')
api.add_resource(service1, '/service1/<username>')
api.add_resource(service2, '/service2/<username>')
api.add_resource(service3, '/service3/<username>')
api.add_resource(service4, '/service4/<username>')
api.add_resource(service5, '/service5/<username>')
api.add_resource(service6, '/service6/<username>')
api.add_resource(service7, '/service7/<username>')
api.add_resource(service8, '/service8/<username>')
api.add_resource(service9, '/service9/<username>')
api.add_resource(service10, '/service10/<username>')



app.run(port=5003)