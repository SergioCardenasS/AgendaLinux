import sqlite3

#Tabla configuration
TABLE_CONFIGURATION 	= 'Configuracion'
KEY_C_V 				= 'Id'
KEY_C_IMAGE_PATH 		= 'Imagen'
#Tabla actividades
TABLE_ACTIVITIES 		= 'Actividades'
KEY_A_ID 				= 'Id'
KEY_A_NAME 				= 'Nombre'
#Tabla tareas
TABLE_TASK 				= 'Tareas'
KEY_T_ID 				= 'Id'
KEY_T_ID_A 				= 'Actividad' 
KEY_T_NAME 				= 'Nombre'
KEY_T_DESCRIPTION 		= 'Descripcion'
KEY_T_MOD_DATETIME 		= 'Fecha_inicio'
KEY_T_FINISH_DATETIME 	= 'Fecha_fin'
KEY_T_FINISHED 			= 'Finalizada'
#Tabla Notificaciones
TABLE_NOTIFICATION 		= 'Notificacion'
KEY_N_ID_T 				= 'Tarea'
KEY_N_MAIN 				= 'Principal'
KEY_N_THREAD 			= 'Hilo'
KEY_N_TURN 				= 'Turno'
KEY_N_STATUS 			= 'Estado'


def connection_data_base():
	conn = sqlite3.connect('dataBase.db')
	return conn
