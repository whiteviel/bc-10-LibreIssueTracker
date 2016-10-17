#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120), index=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    other_name = db.Column(db.String(120))
    role = db.Column(db.Integer)
    verified = db.Column(db.Integer)
    department = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __init__(
            self,
            username,
            email,
            password,
    ):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.nickname


class department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    admin_id = db.Column(db.Integer)

    def __init__(self, name, admin_id):
        self.name = name
        self.admin_id = admin_id


class issue(db.Model):
    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(120))
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.Integer, index=True)
    priority = db.Column(db.Integer, index=True)

    def __init__(
            self,
            title,
            description,
            user,
            status,
            priority,
    ):
        self.title = title
        self.description = description
        self.user = user
        self.status = status
        self.priority = priority