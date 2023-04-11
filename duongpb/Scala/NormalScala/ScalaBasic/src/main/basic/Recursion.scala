import scala.annotation.tailrec

object Recursion extends App {
  def factorial(n: Int): Int =
    if (n <= 1) 1
    else {
      println("something ahead of the result line")
      val  result = n * factorial(n - 1)
      println("something behind of the result line")
      result // return this as it's the last line of the else phrase
    }
    //this way is causing the StackOverFlowError happens when the stack blow up with memory because the recursive is storing the temp value as a return one
    // to prevent this, we need to place the function as a return in the recursive, this is called the TAIL RECURSIVE

  def anotherSmartFactorial(n: Int): Int = {
    @tailrec
    def factHelper(x: Int, accumulator: Int): Int =
      if (x<=1) accumulator
      else factHelper(x-1, x* accumulator) // TAIL RECURSIVE, this way we store the temp value inside the accumulator
    factHelper(n, 1)
  }

  // the key ingredent is to use the function as the final return for the function
  // WHEN YOU NEED LOOPS, USE _TAIL_ RECURSIVE

  /**
   Excercise:
   1. concatenate  a string in times
   2. isPrime function tail recursive
   3. fibonacci function with tail recursive
   **/

  @tailrec
  def concatinateString(aString: String, concatTime: Int, accumulator: String): String =
    if(concatTime <= 0) accumulator
    else concatinateString(aString, concatTime - 1, accumulator + aString)

  println(concatinateString("hello", 3, ""))

  def isPrime(n: Int): Unit = {
    def isPrimeTailRec(t: Int, isStillPrime: Boolean): Boolean =
      if (!isStillPrime) false
      else if (t <= 1) true
      else isPrimeTailRec(t - 1, n % t != 0 && isStillPrime)

      isPrimeTailRec(n / 2, true)
  }

  def finobacci (n: Int): Int= {
    def fiboTailRec(i: Int, last: Int, nextToLast: Int): Int =
      if(i >= n ) last
      else fiboTailRec(i + 1, last + nextToLast, last)

    if(n <= 2) 1
    else fiboTailRec(2, 1, 1)
  }
}
