# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:05:48 by humontas          #+#    #+#              #
#    Updated: 2026/08/17 04:45:16 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import psycopg2

def	get_connection(dbname_, user_, password_, host_):
	conn = psycopg2.connect(
		dbname=dbname_,
		user=user_,
		password=password_,
		host=host_
	)
	cur = conn.cursor()
	return(conn, cur)