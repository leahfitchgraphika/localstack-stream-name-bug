cdklocal bootstrap
cdklocal deploy
awslocal lambda invoke --function-name=get-stream-info get_stream_info.json
cat get_stream_info.json