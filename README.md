# **CI/CD Project**

*Realized by : HADJI Rayan, MOUAZER Rayane - TP1 ILC 4A*

Our GitHubs : 

<a href="url"><img src="https://avatars.githubusercontent.com/u/115188188?v=4" align="left" height="50" width="50" ></a><br> [HADJI Rayan](https://github.com/DZburst)

<a href="url"><img src="https://avatars.githubusercontent.com/u/123754563?s=400&u=722c3e59b954407c8b423b7ebb8b3e3599aa0980&v=4" align="left" height="50" width="50" ></a><br> [MOUAZER Rayane](https://github.com/rayanemouazer) 

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

---

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

  We didn't have any problem for this one, since it was already part of the actions available in the Github Action Library.

* <u>**One triggered manually to use the Dockerfile file, in order to generate an image.**</u>

  We only had to modify 1 or 2 things in the Docker template, available in the library.

* <u>**One triggered for each semver tag to use the Dockerfile file, in order to generate and push the image of the API, its tag being the specified semver version.**</u>

  This is actually the part on which we struggled the most, alongside the CD part. Although we tried several different codes, we only kept on getting errors at first. After several attempts, we were finally able to run the workflow without any error, but there is still a problem which we haven't been able to solve : it doesn't actually push the image to Docker Hub. We also tried to do it manually, from the codespace's terminal with the command `docker push dzburst/ci-cd_project:v1.0.0` ;  but then, it says that no image exists in this repository. So, we guess the issue may come from the way we get the tag, in the *Build and Push Docker Image* workflow, but we don't know how to actually solve it.

## **Part 3 : API & CSV file Documentation**

* **Acquiring *.csv* data**

  Regarding this part of the API, since we had some freedom for the representation and the way we handle the different elements, we've chosen to directly ask for the user to type in the path of the csv file. We're totally aware that this is definitely not the most secure way to do it, but for now we prefer to keep it that way. We've chosen to focus more on the other demands, notably regarding Swagger, Docker and GitHub Actions, for we believe it is part of the fundamentals of this module. Nonetheless, it is for sure a point which would need to be patched in the potential future versions of the API.  
  So basically, in order to load data from a *.csv* file :
  - Put your *.csv* file in the *Ressources* directory
  - Go to the main menu's URL
  - Add the path of your file ( don't forget to escape the necessary characters )
  - Add the name of the calendar you want to generate with your *.csv* file.

  The URL should look like this : ***main_menu_url/path_of_csv_file/name_of_calendar***

  Also, please add headers to the columns of your file if there aren't already some, and rename them as follows :  
  ***Name***, ***Timestamp***, ***Duration***, ***Participants***  
  For now, our code is case-sensitive, so please beware when renaming the columns.

## **Workflow Badges**
[![Build Status](https://github.com/DZburst/CI-CD_Project/workflows/Build%20and%20Push%20Docker%20Image/badge.svg)](https://github.com/DZburst/CI-CD_Project/actions)
[![Build Status](https://github.com/DZburst/CI-CD_Project/workflows/Docker%20Image%20CI/badge.svg)](https://github.com/DZburst/CI-CD_Project/actions)
[![Build Status](https://github.com/DZburst/CI-CD_Project/workflows/Python%20application/badge.svg)](https://github.com/DZburst/CI-CD_Project/actions)

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
