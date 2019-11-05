class Solution:
    def findFavoriteGenres(self, userSongs, SongGenres):
        res = {}

        # classify each song into song_classify
        s_classify = {}
        for s_type in SongGenres:
            for s_index in SongGenres[s_type]:
                s_classify[s_index] = s_type
        if not s_classify: return {}

        # get the result of the person one by one
        for person in userSongs:
            temp = {}

            # If he song of the person has type
            for song in userSongs[person]:
                if song in s_classify:
                    temp[s_classify[song]] = temp.get(s_classify[song], 0) + 1

            # temp is not empty
            if temp.values():
                max_val = max(temp.values())
            for key in temp:
                if temp[key] == max_val:
                    res[person] = res.get(person, []) + [key]
        return res

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
    test = S.findFavoriteGenres({
   "David": ["song1", "song2"],
   "Emma":  ["song3", "song4", "song5"]
},
        {"Pop": ["song5", "song6"],}
    )
    print(test)