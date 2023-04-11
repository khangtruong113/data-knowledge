package main.basic

object Exceptions extends App {
  val x: String = null
  //causing the program to crush

  //throwing and catching exceptions

  //1. throwing an exception

  val aWeirdValue: String = throw new NullPointerException

  //throwable classes extend the Throwable class
  //exception and Error are the major Throwable subtypes

  // 2. how to catch an exceptions
  def getInt(withException: Boolean): Int =
    if(withException) throw new RuntimeException("no int for this time")
    else 42

  try {
    //code that might throw
    getInt(true)
  }
  catch {
    case e: RuntimeException => println("caught a runtime exception")
  }
  finally {
    //finally get execute no matter what
    //optional
    //does not influence the return type of this expression
    //use finally only for side effects
     println("finally")

    //3. custom exception
    class MyException extends Exception
    val exceptions = new MyException

    //we can throw this new exception
    throw exceptions
  }
}
