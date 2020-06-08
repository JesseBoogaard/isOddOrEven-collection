import java.math.BigDecimal;
import java.util.Collections;
import java.util.LinkedHashSet;
import java.util.Set;

/**
 * Contains a method {@link ParallelIsOdd#isOdd} to determine if a number is odd using a safe
 * concurrent algorithm
 * <p>
 * The implementation is well commented
 */
public class ParallelIsOdd {
    /**
     * The is odd boolean
     *
     * @implNote volatile makes concurrency more reliable so this field is volatile
     */
    // isOdd is flipped number times by the threads, to determine if number is odd
    static volatile boolean isOdd = true;
    /**
     * The is odd lock for safety
     *
     * @implNote volatile makes concurrency more reliable so this field is volatile
     */
    /*package*/
    static volatile Object theIsOddLock = new Object() {
        public String toString() {
            return "IsOddLock{isOdd: " + isOdd + "}";
        }
    };
    /**
     * Determines if a number is odd using an efficient and safe concurrent algorithm.
     * <p>
     * Runs in only O(n) time.
     *
     * @param number the number to determine if it is odd using an efficient and safe concurrent algorithm that runs
     *               in only O(n) time
     * @return if the number parameter is odd, determined using an efficient and safe concurrent algorithm that runs
     *               in only O(n) time
     */
    public static synchronized boolean isOdd(Number number) {
        // un negate negative numbers
        if (number.doubleValue() < 0) { // check if a number is negative
            number = BigDecimal.valueOf(0 + -number.longValue()); //make the number non negative by negating the negative number
        }
        isOdd = false; //set the is odd boolean to false
        // the collection to hold all the Threads, synchronized safely
        Set<Thread> threads = Collections.<Thread>synchronizedSet(new LinkedHashSet<Thread>()); //create the threads set
        // create all the threads
        for (int i = 0; i < number.longValue(); i++) { //loop number times
            Thread thread = new Thread() { //create a new thread
                public synchronized void run() { //override the run method
                    //make sure to lock on theIsOddLock to check the isOdd field safely
                    synchronized (theIsOddLock) { // synchronize for safety
                        if (isOdd == true) { //check if is odd is true
                            synchronized (theIsOddLock) { // synchronize for safety
                                isOdd = false; // set the is odd boolean to false
                            }
                        } else if (isOdd == false) { //check if is odd is false
                            synchronized (theIsOddLock) { // synchronize for safety
                                isOdd = true; // set the is odd boolean to true
                            }
                        }
                    }
                }
            };
            threads.add(thread); // add the new thread
        }
        // start all the threads
        for (Thread thread : threads) { //go through all the threads
            thread.start(); //start the thread
        }
        // wait for all the threads
        waiting:
        while (true) { // loop forever using while true
            for (Thread thread : threads) { // go through all the threads
                if (thread.isAlive()) { // if thread is running
                    continue waiting; // continue waiting
                }
            }
            break; // break out of waiting
        }

        threads.clear(); // help the gc by clearing all threads

        return isOdd; //return if the number is odd
    }

    public static void main(String[] args) {
        System.out.println(isOdd(136));
        System.out.println(isOdd(29));
        System.out.println(isOdd(-42));
    }
}
