import json

fileName = "my-data.json"
jsonString = '{ "name": "DelftStack", "email": "DelftStack@domain.com", "age": 20, "country": "Netherlands", "city": "Delft"}'
jsonString = json.loads(jsonString)



context = "[{"id":240614362,"title":"今天大桃園一號","excerpt":"未看先猜，希望他可以不要貪太多就好，運動場用好點","anonymousSchool":false,"anonymousDepartment":false,"pinned":false,"forumId":"255fd275-fec2-49d2-8e46-2e1557ffaeb0","replyId":null,"createdAt":"2022-11-26T04:49:54.154Z","updatedAt":"2022-11-26T04:49:54.154Z","commentCount":1,"likeCount":0,"collectionCount":0,"withNickname":true,"tags":[],"topics":["桃園","有趣","閒聊","政治","台灣"],"meta":{"layout":"classic"},"forumName":"閒聊","forumAlias":"talk","nsfw":false,"gender":"M","school":"雨勢滂薄","department":"waron","replyTitle":null,"reportReason":"","reactions":[],"hidden":false,"customStyle":null,"isSuspiciousAccount":false,"isModerator":false,"layout":"classic","spoilerAlert":false,"withImages":true,"withVideos":false,"media":[{"url":"https://imgur.com/0N9AqRz.jpg"}],"reportReasonText":"","supportedReactions":null,"isSelectedPost":false,"unsafe":false,"enablePrivateMessage":false,"enableNestedComment":true,"totalCommentCount":1,"mediaMeta":[{"id":"6aa56a4b-916e-4d3e-b480-9931f9f5f495","url":"https://i.imgur.com/0N9AqRzl.jpg","normalizedUrl":"https://i.imgur.com/0N9AqRzl.jpg","thumbnail":"https://i.imgur.com/0N9AqRzl.jpg","type":"image/thumbnail","tags":["ANNOTATED"],"createdAt":"2022-11-26T04:49:54.154Z","updatedAt":"2022-11-26T04:49:54.154Z","width":358,"height":628,"croppingWindow":{"anchorX":0,"anchorY":71,"width":358,"height":214},"blurhash":"cbF?9Vr:k:~TsRx]Voslx_o#t6RjbdkDjY"},{"id":"6aa56a4b-916e-4d3e-b480-9931f9f5f495","url":"https://i.imgur.com/0N9AqRz.jpg","normalizedUrl":"https://imgur.com/0N9AqRz","thumbnail":"https://i.imgur.com/0N9AqRzl.jpg","type":"image/imgur","tags":["ANNOTATED"],"createdAt":"2022-11-26T04:49:54.154Z","updatedAt":"2022-11-26T04:49:54.154Z","width":358,"height":628,"croppingWindow":{"anchorX":0,"anchorY":71,"width":358,"height":214},"blurhash":"cbF?9Vr:k:~TsRx]Voslx_o#t6RjbdkDjY"}],"elapsedTime":438,"edited":false,"identityIdV3":"5a70e003-aadd-4534-acf8-30afc79ee5aa","postAvatar":"","activityAvatar":"","verifiedBadge":false,"memberType":""}]"

obj = json.loads(context)

file = open('test.json', "w")
json.dump(obj, file)
file.close()