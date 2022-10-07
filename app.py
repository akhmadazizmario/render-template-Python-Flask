from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pos'
mysql = MySQL(app)


@app.route('/')  # indexnya titik awal mengakses website
def main():
    return render_template('index.html')


@app.route('/masterbarang')
def masterbarang():
    cur = mysql.connection.cursor()
    cur.execute("SELECT*FROM masterbarang")
    barang = cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', data=barang)


@app.route('/mastersuplier')
def mastersuplier():
    return render_template('mastersuplier.html')


@app.route('/masterpelanggan')
def masterpelanggan():
    return render_template('masterpelanggan.html')


@app.route('/formpembelian')
def formpembelian():
    return render_template('formpembelian.html')


@app.route('/datapembelian')
def datapembelian():
    return render_template('datapembelian.html')


@app.route('/formpenjualan')
def formpenjualan():
    return render_template('formpenjualan.html')


@app.route('/datapenjualan')
def datapenjualan():
    return render_template('datapenjualan.html')


if __name__ == "__main__":
    app.run(debug=True)
