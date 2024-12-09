##
## EPITECH PROJECT, 2024
## tradingbot
## File description:
## Makefile
##

ANALYZER_NAME 	=	my_torch_analyzer
GENERATOR_NAME 	=	my_torch_generator

ANALYZER_MAIN 	=	src/analyzer/main.py
GENERATOR_MAIN 	=	src/generator/main.py

all: $(ANALYZER_NAME) $(GENERATOR_NAME)

$(ANALYZER_NAME):
	@echo -ne "\nCompilation: "
	cp $(ANALYZER_MAIN) $(ANALYZER_NAME)
	chmod +x $(ANALYZER_NAME)
	@echo -e "\033[92mDone\n\033[0m"

analyzer_clean:
	@echo -ne "Clean: \n"
	rm -rf $(ANALYZER_NAME)
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

fclean: analyzer_clean generator_clean

re:	fclean all
