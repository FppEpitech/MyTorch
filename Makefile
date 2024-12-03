##
## EPITECH PROJECT, 2024
## tradingbot
## File description:
## Makefile
##

ANALYSER_NAME 	=	my_torch_analyzer
GENERATOR_NAME 	=	my_torch_generator

ANALYSER_MAIN 	=	src/analyser/main.py
GENERATOR_MAIN 	=	src/generator/main.py

all: $(ANALYSER_NAME) $(GENERATOR_NAME)

$(ANALYSER_NAME):
	@echo -ne "\nCompilation: "
	cp $(ANALYSER_MAIN) $(ANALYSER_NAME)
	chmod +x $(ANALYSER_NAME)
	@echo -e "\033[92mDone\n\033[0m"

analyser_clean:
	@echo -ne "Clean: \n"
	rm -rf $(ANALYSER_NAME)
	@echo -e "\033[92m Done\033[0m"

$(GENERATOR_NAME):
	@echo -ne "\nCompilation: "
	cp $(GENERATOR_MAIN) $(GENERATOR_NAME)
	chmod +x $(GENERATOR_NAME)
	@echo -e "\033[92mDone\n\033[0m"

generator_clean:
	@echo -ne "Clean: \n"
	rm -rf $(GENERATOR_NAME)
	@echo -e "\033[92m Done\033[0m"

clean:

fclean: analyser_clean generator_clean

re:	fclean all
