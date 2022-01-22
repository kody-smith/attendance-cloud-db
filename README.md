# Overview

This software is an attendance tracking system meant to aid teachers and professors in understanding the preparedness of their students. The program can access data regarding students located in a cloud database including their name, email address, age, student ID, and other relevant information. The goal of this program is to provide teachers and professors with necessary information regarding their students so they can know which students need the most assistance and how to best assist them.

[Software Demo Video](https://youtu.be/I9814mprU5w)

# Cloud Database

The cloud database service used is firestore. The database contains collections of students and modules by week. These collections have documents that hold data pertaining to the students and module topics and assignments.

# Development Environment

I developed this software in Visual Studio Code using python. In order to directly access the database you need to import the firebase admin library. This allows you to view, insert, and modify data directly in Visual Studio Code.

# Useful Websites

Below are some resources available to aid in creating a cloud database and manipulating it.

* [Firebase](https://firebase.google.com/docs)
* [Firebase Managing data structures](https://firebase.google.com/docs/firestore/manage-data/structure-data)

# Future Work

Some things that I would like to add to this program is the ability to also generate a score of preparedness based on grades as well as attendance.