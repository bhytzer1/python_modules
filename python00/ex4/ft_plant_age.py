# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmandric <dmandric@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/04 23:29:14 by dmandric          #+#    #+#              #
#    Updated: 2026/04/04 23:35:19 by dmandric         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age() -> None:
	plant_age = int(input("Enter plant age in days:"))
	if(plant_age > 60):
		print(f"Plant is ready to harvest!")
	else:
		print(f"Plant needs more time to grow.")
