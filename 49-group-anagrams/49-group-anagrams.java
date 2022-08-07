class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> closedColission = new HashMap<>();
        for(String str : strs) {
            char[] strArr = str.toCharArray();
            Arrays.sort(strArr);
            String sorted = String.valueOf(strArr);
            if (!closedColission.containsKey(sorted)) {
                closedColission.put(sorted, new ArrayList<>());
            }
            closedColission.get(sorted).add(str);
        }
        return new ArrayList<>(closedColission.values());
    }
}