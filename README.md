# **CI/CD Project**

*Realized by : HADJI Rayan, MOUAZER Rayane - TP1 ILC 4A*

## **Part 1 : Routes to implement**

* <u>**E1: Add an event to the calendar**</u>

  For this route, we struggled a bit at the beginning since we still weren't used to how Flask works. For instance, we had some issues regarding user's input. However, we actually decided to go with the variables being directly typed in the route, since it was easier for us.  
  Also, regarding the representation of our calendar, we started with a very simple one : we only used strings.

* <u>**E2: Display all the events of the calendar in chronological order**</u>

  This is probably one of the tasks with which we struggled the most. Actually, Rayane M. did it quite quickly, and it seemed to work fine on his laptop. But then, when I tried it, it didn't seem to work on my PC. After a lot of pointless modifications, I had no choice but to ask ChatGPT, which pointed out the fact that it might be related to the browser used. Indeed, when I printed in the terminal the calendar before and after sorting, the result was the right one. But once Flask displayed it in the corresponding endpoint, it actually sorted the calendar in chronological order based on the keys, by default. We thus had to replace *jsonify(cal)* by *json.dumps()* and set its *sort_keys* parameter to False. Although the display is no more the same as for the other endpoints, it now actually shows the sorted calendar as expected.  
  Also, while Rayane M. was taking care of this route and the following, I changed the initial representation to have a cleaner code, by using a class for events. We thus created a new branch, in case we had some fatal issue with this changement ; after a few attempts, we were finally able to merge it with both of our branches.

* <u>**E3 : Display the events associated to a given participant in chronological order**</u>

* <u>**E4 : Add a participant to an event**</u>

* <u>**E5 : Display the details of the next event**</u>

* <u>**E6 : Import data from a *.csv* file**</u>

  After having looked at how to generally acquire data from a csv table in Python, we tried to adapt to our situation. At first, we were planning on using only 1 parameter in the route, which corresponds to the path of the *.csv* file. But to actually make the code simpler, and also have a better overall representation, we finally chose to add another global variable, which is a dictionary that contains all the calendars used. Thus, not only the access is easier - both in the code and for users -, but it also allows one to store several calendars rather than only one.  
  The main problem we had with the code of this endpoint was the fact that the return value was actually an empty dictionary. After several tests with prints, we noticed that the if statement to acquire the data of each row, was actually always false. Indeed, *\ufeff* was automatically added at the beginning of the $1^{\text{st}}$ column, right before *Name*. So, we had to get rid of it using *codecs* and *'utf-8-sig'*.


## **Part 2 : GitHub Actions for Continuous Integration**

Create 3 GitHub Actions :  
* <u>**One triggered by any change to build the application.**</u>


* <u>**One triggered manually to use the Dockerfile file, in order to generate an image.**</u>


* <u>**One triggered for each semver tag to use the Dockerfile file, in order to generate and push the image of the API, its tag being the specified semver version.**</u>


## **Part 3 : API & CSV file Documentation**

* **Acquiring *.csv* data**

  Regarding this part of the API, since we had some freedom for the representation and the way we handle the different elements, we've chosen to directly ask for the user to type in the path of the csv file. We're totally aware that this is definitely not the most secure way to do it, but for now we prefer to keep it that way. We've chosen to focus more on the other demands, notably regarding Swagger, Docker and GitHub Actions, for we believe it is part of the fundamentals of this module. Nonetheless, it is for sure a point which would need to be patched in the potential future versions of the API.  
  So basically, in order to load data from a *.csv* file :  
  - Go to the main menu's URL
  - Add the path of your file, making sure it is within the scope of the API ( don't forget to escape the necessary characters )
  - Add the name of the calendar you want to generate with your *.csv* file.

  The URL should look like this : ***main_menu_url/path_of_csv_file/name_of_calendar***

  Also, please add headers to the columns of your file if there aren't already some, and rename them as follows :  
  ***Name***, ***Timestamp***, ***Duration***, ***Participants***  
  For now, our code is case-sensitive, so please beware when renaming the columns.


# **Appendix**

## **Common URL Escape values :**
  
  |  Character  |  URL Escape  |
  |-------------|--------------|
  |    SPACE    |      %20     |
  |      /      |      %2F     |
  |      \      |      %5C     |
  |      $      |      %24     |
  |      %      |      %25     |
  |      &      |      %26     |
  |      ?      |      %3F     |