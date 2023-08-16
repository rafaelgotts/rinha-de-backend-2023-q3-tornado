build:
	@docker build . -t rinha-api-tornado -t rafaelgotts/rinha-api-2023-tornado
	@docker push rafaelgotts/rinha-api-2023-tornado:latest

run:
	@docker run --network=host rinha-api-tornado
