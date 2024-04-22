from main_lib import * 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/account/all', methods=['GET'])
def get_all_account():
    # Kết nối đến MySQL
    cnx = mysql.connector.connect(user='root', 
                                password='JohnnyTr@n1101',
                                host='localhost',
                                port='3307',
                                database='test')

    # Tạo một đối tượng cursor
    cursor = cnx.cursor()

    # Lấy dữ liệu
    cursor.execute("""
    SELECT * FROM User
    """)

    # Lấy kết quả truy vấn
    results = cursor.fetchall()

    # Chuyển đổi kết quả truy vấn thành danh sách các từ điển
    data = [dict(zip(cursor.column_names, row)) for row in results]

    # Đảm bảo dữ liệu được commit
    cnx.commit()

    # Đóng kết nối
    cursor.close()
    cnx.close()

    return jsonify(data)
    
@app.route('/api/account/create', methods=['GET'])
def create_account():
    # Kết nối đến MySQL
    cnx = mysql.connector.connect(user='root', 
                                password='JohnnyTr@n1101',
                                host='localhost',
                                port='3307',
                                database='test')

    # Tạo một đối tượng cursor
    cursor = cnx.cursor()

    # Tạo bảng
    try:
        cursor.execute("""
        CREATE TABLE User (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50)
        )
        """)
    except Exception:
        print('Cannot create User table')

    # Thêm dữ liệu
    cursor.execute("""
    INSERT INTO User (name) VALUES ('Nguyen Van A')
    """)

    # Đảm bảo dữ liệu được commit
    cnx.commit()

    # Đóng kết nối
    cursor.close()
    cnx.close()

    return Response('Account added')

@app.route('/', methods=['GET'])
def index():
    return Response('BE Hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

