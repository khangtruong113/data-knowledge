package main.functional



import scala.util.{Failure, Success, Try}

object HandlingFailure extends App {
  //create success and failure
  val aSuccess = Success(3)
  val aFailure = Failure(new RuntimeException("Suprttttttt Failure"))

  println(aSuccess)
  println(aFailure)

  def unsafeMethod(): String = throw new RuntimeException("No String")

  //try objhect via the apply method, call an unsafe method
  val potentialFAilure = Try(unsafeMethod())
  println(potentialFAilure)

  //syntax sugar
  val anotherPotentialFailure = Try {
    //code that might throw exception
  }

  //utilities
  println(potentialFAilure.isSuccess) //tell if this success or not, if it has an exception inside, it will be false

  //or else
  def backupMethod(): String = "a valid result"

  val fallbackTry = Try(unsafeMethod()).orElse(Try(backupMethod()))

  //IF YOU DESIGN THE API, if you know your code is throwing exception
  def betterUnsafeMethod(): Try[String] = Failure(new RuntimeException)
  def betterBackupMethod() : Try[String]= Success("a valid one")
  val betterFallBack = betterUnsafeMethod() orElse betterBackupMethod()

  //map, flatmap + filter

  println(aSuccess.map(_*2))
  print(aSuccess.flatMap(x => Success(x*10)))
  println(aSuccess.filter(_ > 10 ))

  //for comprehension as well

}
