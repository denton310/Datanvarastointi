from flask import Flask, request, jsonify
import db

app = Flask(__name__, static_url_path='')
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
	message = {
		'status': 200,
		'message': 'Hello from Company!' ,
    }
	resp = jsonify(message)
	resp.status_code = 200    
	return resp	

#
@app.route('/employees', methods=['GET'])
def employees():
	try:
		conn = db.createConnetion()
		cursor = conn.cursor()
		sql = """
            SELECT fname, lname, 
	            CAST(bdate AS char) as bdate, 
		        salary, phone1  
	        FROM employee
            ORDER BY lname
        """
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.close() 
		conn.close()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		message = {
        	'status': 500,
        	'message': f'{e}'
    	}
		resp = jsonify(message)
		resp.status_code = 500
		return resp

@app.route('/department', methods=['GET'])
def department():
	try:
		conn = db.createConnetion()
		cursor = conn.cursor()
		sql = """
            SELECT d.name AS department, e.fname, e.lname
			FROM department d, employee e
			WHERE d.manager_id = e.id
        """
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.close() 
		conn.close()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		message = {
        	'status': 500,
        	'message': f'{e}'
    	}
		resp = jsonify(message)
		resp.status_code = 500
		return resp

@app.route('/projects', methods=['GET'])
def projects():
	try:
		conn = db.createConnetion()
		cursor = conn.cursor()
		sql = """
            SELECT p.name
			FROM project p
        """
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.close() 
		conn.close()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		message = {
        	'status': 500,
        	'message': f'{e}'
    	}
		resp = jsonify(message)
		resp.status_code = 500
		return resp

@app.route('/works_on', methods=['GET'])
def works_on():
	try:
		conn = db.createConnetion()
		cursor = conn.cursor()
		sql = """
            SELECT e.fname, e.lname, p.name as project, wo.hours
			FROM employee e, project p, works_on wo
			WHERE e.id = wo.employee_id AND wo.project_id = p.id	
        """
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.close() 
		conn.close()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		message = {
        	'status': 500,
        	'message': f'{e}'
    	}
		resp = jsonify(message)
		resp.status_code = 500
		return resp	

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404    
    return resp
		
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
