import json


with open('./data/nycu11-27.json', 'r', encoding='UTF-8') as f:
    list_data = json.load(f)

    #print(list_data)
    print(len(list_data))
    print(list_data[0])

    for key, value in list_data[0].items():
        print(key)

    

''' 
key:
id
title
excerpt
anonymousSchool
anonymousDepartment
pinned
forumId
replyId
createdAt
updatedAt
commentCount
likeCount
collectionCount
withNickname
tags
topics
meta
forumName
forumAlias
nsfw
gender
school
replyTitle
reportReason
reactions
hidden
customStyle
isSuspiciousAccount
isModerator
layout
spoilerAlert
withImages
withVideos
media
reportReasonText
supportedReactions
isSelectedPost
unsafe
enablePrivateMessage
enableNestedComment
totalCommentCount
mediaMeta
edited
postAvatar
activityAvatar
verifiedBadge
memberType

'''