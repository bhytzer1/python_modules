# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dmandric <dmandric@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/04 23:19:44 by dmandric          #+#    #+#              #
#    Updated: 2026/04/04 23:27:46 by dmandric         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total() -> None:
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {harvest1 + harvest2 + harvest3}")
