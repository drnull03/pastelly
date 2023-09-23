

run:
	@xterm -e "bash -c 'export FLASK_APP=app.py && flask run' "

exit:
	@pkill -f "flask run"

