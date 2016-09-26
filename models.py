#!/usr/bin/env python
import sqlite3
from constants import *

db = connection_data_base()

CREATE_CONFIGURATION_TABLE = "CREATE TABLE " + TABLE_CONFIGURATION + "(" + KEY_C_V + " INTEGER," + KEY_C_IMAGE_PATH + " TEXT)"

db.execute(CREATE_CONFIGURATION_TABLE)

INSERT_CONFIGURATION_OPTION_DEFAULT = ("INSERT INTO "+TABLE_CONFIGURATION+" VALUES (1,'')")

db.execute(INSERT_CONFIGURATION_OPTION_DEFAULT);

CREATE_ACTIVITIES_TABLE = ("CREATE TABLE " + TABLE_ACTIVITIES + " ("
                + KEY_A_ID  + " INTEGER PRIMARY KEY AUTOINCREMENT,"
                + KEY_A_NAME + " TEXT)")

db.execute(CREATE_ACTIVITIES_TABLE)

CREATE_TASK_TABLE = ("CREATE TABLE " + TABLE_TASK + " ("
                + KEY_T_ID  + " INTEGER PRIMARY KEY AUTOINCREMENT,"
                + KEY_T_ID_A  + " INTEGER,"
                + KEY_T_NAME + " TEXT,"
                + KEY_T_DESCRIPTION + " TEXT,"
                + KEY_T_MOD_DATETIME + " DATETIME,"
                + KEY_T_FINISH_DATETIME + " DATETIME,"
                + KEY_T_FINISHED + " INTEGER)")
db.execute(CREATE_TASK_TABLE)

CREATE_NOTIFICATIONS_TABLE = ("CREATE TABLE " + TABLE_NOTIFICATION + " ("
                + KEY_N_ID_T  + " INTEGER,"
                + KEY_N_MAIN  + " INTEGER,"
                + KEY_N_THREAD  + " INTEGER,"
                + KEY_N_TURN  + " INTEGER,"
                + KEY_N_STATUS + " INTEGER)")

db.execute(CREATE_NOTIFICATIONS_TABLE)

db.close()