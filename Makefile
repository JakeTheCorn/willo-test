start:
	@python3 main.py
install:
	@pip3 install flask
unit-test:
	@python3 pass_through.test.py
	@python3 format_data.test.py