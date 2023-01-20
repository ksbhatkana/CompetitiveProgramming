public static int diagonalDifference(List<List<Integer>> arr) {
    // Write your code here
    int mdSum = 0, sdSum = 0,md=0,sd=arr.size()-1;
    for(int i = 0; i< arr.size();i++){
        mdSum+=arr.get(i).get(md++);
        sdSum+=arr.get(i).get(sd--);
    }
    return Math.abs(mdSum-sdSum);
}
