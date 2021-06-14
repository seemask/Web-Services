from flask import Flask, jsonify, request, render_template
import re
import datetime
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom
from flask_cors import CORS
import requests
from flask_restplus import  Resource

app = Flask(__name__)

@app.route('/service1',methods=['GET'])
class service1(Resource):
    def get_userdetails1():
        #username = request.args.get('name')
        if re.search(pattern, username[0]): # in A-M return JSON
            JSON_Details['name']=username
            current_time=datetime.datetime.now()
            JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
            JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
            print(JSON_Details)
            return jsonify(JSON_Details)
        elif re.search(pattern1, username[0]):
            current_time = datetime.datetime.now()
            invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
            invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

api.add_resource(service1, 'http://127.0.0.1:5002/service1')

'''
@app.route('/service2',methods=['GET'])
def get_userdetails2():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service3',methods=['GET'])
def get_userdetails3():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service4',methods=['GET'])
def get_userdetails4():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service5',methods=['GET'])
def get_userdetails5():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service6',methods=['GET'])
def get_userdetails6():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service7',methods=['GET'])
def get_userdetails7():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service8',methods=['GET'])
def get_userdetails8():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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

@app.route('/service10',methods=['GET'])
def get_userdetails10():
    username=request.args.get('name')
    print(username)
    if re.search(pattern, username[0]): # in A-M return JSON
        JSON_Details['name']=username
        current_time=datetime.datetime.now()
        JSON_Details['date']=str(current_time.month)+"/"+str(current_time.day)+"/"+str(current_time.year)
        JSON_Details['time']=str(current_time.hour)+"Hr"+str(current_time.minute)+"Min"+str(current_time.second)+"Sec"
        print(JSON_Details)
        return jsonify(JSON_Details)
    elif re.search(pattern1, username[0]):
        current_time = datetime.datetime.now()
        invocation_date = str(current_time.month) + "/" + str(current_time.day) + "/" + str(current_time.year)
        invocation_time = str(current_time.hour) + "Hr" + str(current_time.minute) + "Min" + str(current_time.second) + "Sec"

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


'''



app.run(port=5002)
