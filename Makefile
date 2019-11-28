NAME=get_data

*.zip: $(NAME).py
	zip -r ../$(NAME).zip .

deploy: ../$(NAME).zip
	aws s3 cp ../$(NAME).zip s3://lambda-sample-rafee/$(NAME)/
	aws lambda update-function-code --function-name $(NAME) --s3-bucket \
	lambda-sample-rafee --s3-key $(NAME)/$(NAME).zip