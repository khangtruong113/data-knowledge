import sun.font.TrueTypeFont

/** app is only for intelliJ to run this class */
object Functions extends App {
  def aFunction(a: String, b: Int): String = {
    a + " " + b
  }
  //we can also delete the return type of the expression

  println(aFunction("hello", 3))

  def aParameterlessFunction(): Int = 42

  println(aParameterlessFunction())
  // both calling is fine

  def aRepeatedFunction(aString: String, n: Int): String = {
    if (n == 1) aString
    else aString + aRepeatedFunction(aString, n-1)
  }

  // intelliJ can spot this function as recursive function

  println(aRepeatedFunction("hello", 3))

  // WHEN you need LOOPS, use RECURSION, dont use the normal Loops which returning unit
  def aFunctionWithSideEffects(aString: String) : Unit = println(aString)

  def aBigFunction(n: Int): Int = {
    def aSmallerFunction(a: Int, b: Int): Int = a + b

    aSmallerFunction(n, n-1)
  }

  /**
   example:
   1. a greeting function(name, age) -> " Hi, my name is $name and I m $age years old"
   2. Factorial function : 1 * 2 * 3 * ... * n -> recursive function
   3. Finobaci function : f(1) = 1, f(2) = 1, f(n) = f(n-1) + f(n-2)
   4. tests if a number is prime
   */

  //1 function
  def greetingForKids(name: String, age: Int): String = "Hello my name is " + name + " and I 'm " + age

  def factorial(n: Int): Int =
    if (n == 1) n
    else n * factorial(n-1)

  def finobaci(n: Int): Int =
    if (n <= 2) 1
    else finobaci(n - 1) + finobaci(n - 2)

  def isPrime(n: Int): Boolean = {
    def isPrimtUntil(t: Int): Boolean =
      if (t <= 1) true
      else n % t != 0 && isPrimtUntil(t-1)
    isPrimtUntil(n /2)
  }

}
