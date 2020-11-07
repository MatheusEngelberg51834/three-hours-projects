{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lexfridman\n",
      "lexfridman ------> \n",
      "\n",
      "[['viewCount', '47069365'], ['subscriberCount', '687000'], ['hiddenSubscriberCount', False], ['videoCount', '496']] \n",
      "\n",
      "\n",
      "\n",
      "Lex Fridman Podcast - Solo Episodes\n",
      "----------------------------------------------------------------------\n",
      "Short Lex Videos\n",
      "----------------------------------------------------------------------\n",
      "Ask Me Anything (AMA) with Lex Fridman\n",
      "----------------------------------------------------------------------\n",
      "Lex Fridman Podcast Clips\n",
      "----------------------------------------------------------------------\n",
      "Self-Driving Cars Lectures\n",
      "----------------------------------------------------------------------\n",
      "Life and Fitness\n",
      "----------------------------------------------------------------------\n",
      "Music and Poetry\n",
      "----------------------------------------------------------------------\n",
      "AI Quick Insights\n",
      "----------------------------------------------------------------------\n",
      "Lex Fridman Podcast\n",
      "----------------------------------------------------------------------\n",
      "Deep Learning Lectures\n",
      "----------------------------------------------------------------------\n",
      "Deep Learning School 2016: Individual Talks\n",
      "----------------------------------------------------------------------\n",
      "Research\n",
      "----------------------------------------------------------------------\n",
      "Take It Uneasy Podcast\n",
      "----------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "#####enter api key##########################\n",
    "\n",
    "api_key = ''\n",
    "\n",
    "from googleapiclient.discovery import build\n",
    "\n",
    "channels = input().split()\n",
    "ids = []\n",
    "\n",
    "service = build('youtube', 'v3', developerKey=api_key)\n",
    "\n",
    "\n",
    "for user_name in channels:\n",
    "######## use entered user ids to get the channel id ###################\n",
    "    request = service.channels().list(\n",
    "            part = 'contentDetails, statistics',\n",
    "            forUsername = user_name\n",
    "        )\n",
    "\n",
    "    response = request.execute()\n",
    "\n",
    "    for item in response['items']:\n",
    "        statistics = []\n",
    "        statistics_dict = item['statistics']\n",
    "        statistics.append(['viewCount',statistics_dict['viewCount']])\n",
    "        statistics.append(['subscriberCount',statistics_dict['subscriberCount']])\n",
    "        statistics.append(['hiddenSubscriberCount',statistics_dict['hiddenSubscriberCount']])\n",
    "        statistics.append(['videoCount',statistics_dict['videoCount']])\n",
    "        print(user_name,'------>', '\\n')\n",
    "        print(statistics, '\\n')\n",
    "        ids.append(item['id'])\n",
    "        \n",
    "for id_ in ids:\n",
    "####### use the ids to get the playlist names####################\n",
    "        request = service.playlists().list(\n",
    "            part = 'contentDetails, snippet',\n",
    "            channelId = id_,\n",
    "            maxResults = 50\n",
    "        )\n",
    "    \n",
    "        response = request.execute()\n",
    "        \n",
    "        print()\n",
    "        print()\n",
    "        for item in response['items']:\n",
    "            print(item['snippet']['title'])\n",
    "            print('----------------------------------------------------------------------')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
