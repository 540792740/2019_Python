import collections

class Solution:
    def findFavoriteGenres(self, userSongs, SongGenres):
        res = {}

        # classify each song into song_classify, values is the type of song
        s_classify = {}
        for s_type in SongGenres:
            for s_index in SongGenres[s_type]:
                s_classify[s_index] = s_type
        print(s_classify)
        for person in userSongs:
            temp = {}
            for song in userSongs[person]:
                temp[s_classify[song]] = temp.get(s_classigy[song], 0) + 1
                print(temp)




if __name__ == '__main__':
    S = Solution()
    test = S.findFavoriteGenres({
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
        {
            "Rock": ["song1", "song3"],
            "Dubstep": ["song7"],
            "Techno": ["song2", "song4"],
            "Pop": ["song5", "song6"],
            "Jazz": ["song8", "song9"]
        })
    print(test)
#     test = S.findFavoriteGenres({
#    "David": ["song1", "song2"],
#    "Emma":  ["song3", "song4"]
# }, {}
#     )
    print(test)