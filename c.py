import streamlit as st
import mysql.connector as cn
conn=cn.connect(user="root",host="localhost",password="root",database="python")
cur=conn.cursor()
#cur.execute('create table emp(id int not null auto_increment primary key,name text, age int )')
#st.write('created successfully')
#a=st.text_input("inter name")
#b=st.text_input("enter age")
#print(a)
#st.write(a)
with st.form("insert_data"):
    name =st.text_input("name")
    age = st.text_input("age")
    submit_button = st.form_submit_button("insert data")
    a=st.form_submit_button("view data")
    #b=st.form_submit_button('update data')

if submit_button:
    query = "insert into emp (name, age) values(%s, %s)"
    cur.execute(query,(name,age))
    conn.commit()
    st.success('data witten successfully')
    st.balloons()
    #a=st.button("view data")
if  a:

    cur.execute("select * from emp")

    for i in cur:
        st.write(i)
st.write("update data")
user_id = st.text_input("enter id")
new_name = st.text_input("enter name")
new_age = st.text_input("enter age")
b=st.button('update data')
    
if b:
    
    query ="update emp set name =%s, age = %s where id= %s "
    cur.execute(query,(new_name,new_age,user_id))
    conn.commit()
    st.success("updated succesfully")

d_id=st.text_input("enter your id")
if st.button("delete data"):
    q="delete from emp where id=%s"
    cur.execute(q,(d_id,))
    conn.commit()
    st.success("delete succesfull")