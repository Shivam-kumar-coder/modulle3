import streamlit as st
import mysql.connector as cn
#a=st.text_input("enter username")
#b=st.text_input("enter your pasword"
cnn=cn.connect(host="localhost",user="root",password="root",database="python")
cur=cnn.cursor()
#cur.execute("create table student(id int auto_increment primary key, name text, class int, age int)")
with st.form("student registration"):
    a=st.text_input("enter your name")
    b=st.number_input("enter your class")
    c=st.number_input("enter your age")
    value=(a,b,c)
    query="insert into student (name,class,age) values(%s,%s,%s)" 
    button=st.form_submit_button("submit")

if button:
    cur.execute(query,value)
    cur.execute("commit")
    cur.execute("select * from student")
    st.success("data inserted")
    a=st.button("view data")
if a:
    st.write("your submited entry")
    st.markdown(f"name={a}")
    st.markdown(f"class={b}")
    st.markdown(f"age={c}")
