public class Main {

    private static boolean isEven(String num){
        final char [] numArray = num.toCharArray();
        String value = "0";
        int size = 10 ^ numArray.length;
        for (char d : numArray){
            value = (String) Integer.toString((int) d + Integer.parseInt(value) * size);
            size /= 10;

        }
        if (value.substring(0, 1) == "-"){
            value = value.substring(1, value.length() - 1);
        }
        System.out.println("Calculating...");

        for (int j = Integer.MAX_VALUE; j > -5; j-=2){
            value = Integer.toString(Integer.parseInt(value) - 2);
            if (value.equals("0")){
                return true;
            }

        }

        return false;

    }


    public static void main(String [] args){
        System.out.println(isEven("30"));
        System.out.println(isEven("29"));


    }



}
