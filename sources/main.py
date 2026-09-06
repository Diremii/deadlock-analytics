# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: humontas <humontas@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 04:07:20 by humontas          #+#    #+#              #
#    Updated: 2026/09/06 12:52:17 by humontas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import date

from pipeline import run_pipeline


print(f"Data available from 2026-07-30 to the present ({date.today()})")
print(
	"\n⚠️ WARNING ⚠️\n"
	"The larger the selected date range, the more data will be retrieved.\n"
	"This may increase the retrieval time and the amount of disk space\n"
	"required by the database on your machine.\n"
)

run_pipeline()
