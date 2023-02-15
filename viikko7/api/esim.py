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
