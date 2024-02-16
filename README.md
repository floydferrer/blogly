# SQLAlchemy Part 1

# **Blogly**

[Download exercise](https://curric.springboard.com/software-engineering-career-track/default/exercises/flask-blogly.zip)

This is a multi-unit exercise to practice SQLAlchemy with relationships. Each part corresponds to a unit so make sure that you complete one part and then go onto the next unit.

In it, you’ll build “Blogly”, a blogging application.

## **Part One**

### **Installing Tools**

```bash
(env) $ pip install psycopg2-binary
(env) $ pip install flask-sqlalchemy
```

### **Create User Model**

![graphviz-ccdc089eca5c082609c66f8dd24492c2d0d3d178.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac5e0418-b00c-4630-9e15-e30966971361/graphviz-ccdc089eca5c082609c66f8dd24492c2d0d3d178.svg)

First, create a ***User*** model for SQLAlchemy. Put this in a ***models.py*** file.

It should have the following columns:

- ***id***, an autoincrementing integer number that is the primary key
- ***first_name*** and ***last_name***
- ***image_url*** for profile images

Make good choices about whether things should be required, have defaults, and so on.

### **Create Flask App**

Next, create a skeleton Flask app. You can pattern match from the lecture demo.

It should be able to import the ***User*** model, and create the tables using SQLAlchemy. Make sure you have the FlaskDebugToolbar installed — it’s especially helpful when using SQLAlchemy.

### **Make a Base Template**

Add a base template with slots for the page title and content. Your other templates should use this.

You can use Bootstrap for this project, but don’t spend a lot of time worrying about styling — this is **not** a goal of this exercise.

### **User Interface**

Here is what you should build:

1. **User Listing**

![list.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/848abbd6-ee81-438d-9f93-b6739df62d20/list.png)

2. **New User Form**

![new.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f793ac53-a4d8-4e36-8a65-8e4adcc2c0cc/new.png)

3. **User Detail Page**

![detail.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1141fb30-c990-4440-b3b1-081a04246ba0/detail.png)

4. **User Edit Page**

![edit.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1b27f66-7eb4-4deb-af28-ce1f3ee17198/edit.png)

### **Make Routes For Users**

<aside>
💡 **Note: We Won’t Be Adding Authentication.** While this appliction will have “users”, we’re not going to be building login/logout, passwords, or other such thing in this application. Any visitor to the site should be able to see all users, add a user, or edit any user.

</aside>

**Make routes for the following:**

**GET */ :*** Redirect to list of users. (We’ll fix this in a later step).

**GET */users :*** Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form.

**GET */users/new :*** Show an add form for users

**POST */users/new :*** Process the add form, adding a new user and going back to ***/users***

**GET */users/[user-id] :***Show information about the given user. Have a button to get to their edit page, and to delete the user.

**GET */users/[user-id]/edit :*** Show the edit page for a user. Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

**POST */users/[user-id]/edit :***Process the edit form, returning the user to the ***/users*** page.

**POST */users/[user-id]/delete :*** Delete the user.

### **Add Testing**

Add python tests to at least 4 of your routes.

## **Part One: Further Study**

There are two more big parts to this exercise—but if you feel like you’re ahead of the group, here is some further study for this part you can work on.

### **Add Full Name Method**

It’s likely that you refer to users by `{{ user.first_name }} {{ user.last_name }}` in several of your templates. This is mildly annoying to have to keep writing out, but a big annoyance awaits: what would happen if you added, say, a ***middle_name*** field? You’d have to find & fix this in every template.

Better would be to create a convenience method, ***get_full_name()***, which you could use anywhere you wanted the users’ full name:

```sql
>>> u = User.query.first()

>>> u.first_name    # SQLAlchemy attribute
'Jane'

>>> u.last_name     # SQLAlchemy attribute
'Smith'

>>> u.get_full_name()
'Jane Smith'
```

Write this.

Change your templates and routes to use this.

### **List Users In Order**

Make your listing of users order them by ***last_name***, ***first_name***.

You can have SQLAlchemy do this—you don’t need to do it yourself in your route.

### **Turn Full Name Into a “Property”**

Research how to make a Python “property” on a class — this is something that is *used like* an attribute, but actually is a method. This will let you do things like:
>>> u = User.query.first()

>>> u.first_name    # SQLAlchemy attribute
'Jane'

>>> u.last_name     # SQLAclhemy attribute
'Smith'

>>> u.full_name     # "property"
'Jane Smith'


# One to Many- Blogly

# **Blogly**

## **Part Two: Adding Posts**

In this part, we’ll add functionality for blog posts using the one-to-many features of SQLAlchemy.

### **Post Model**

![Screen Shot 2023-05-08 at 3.00.51 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb6a9d04-b084-48a3-b72f-020047802271/Screen_Shot_2023-05-08_at_3.00.51_PM.png)

Next, add another model, for blog posts (call it ***Post***).

Post should have an:

- ***id***, like for ***User***
- ***title***
- ***content***
- ***created_at*** a date+time that should automatically default to the when the post is created
- a foreign key to the ***User*** table

### **User Interface**

Here is what you should build:

1. **Better User Detail**

![user-w-posts.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e93f8ff7-04ff-4ec7-b0f7-cec22a5f308e/user-w-posts.png)

2. **New Post Form**

![add-post.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/740c1c4f-b709-429c-8c09-b14824dbdaaf/add-post.png)

3. **Post Detail Page**

![detail-post.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5fc525e7-3a42-4059-9418-076af814b31f/detail-post.png)

4. **Post Edit Page**

![edit-post.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e8fe6a75-9cbc-4d3e-8756-a861e08a435c/edit-post.png)

### **Add Post Routes**

**GET */users/[user-id]/posts/new :*** Show form to add a post for that user.

**POST */users/[user-id]/posts/new :*** Handle add form; add post and redirect to the user detail page.

**GET */posts/[post-id] :*** Show a post. Show buttons to edit and delete the post.

**GET */posts/[post-id]/edit :*** Show form to edit a post, and to cancel (back to user page).

**POST */posts/[post-id]/edit :*** Handle editing of a post. Redirect back to the post view.

**POST */posts/[post-id]/delete :*** Delete the post.

### **Change the User Page**

Change the user page to show the posts for that user.

### **Testing**

Update any broken tests and add more testing

### **Celebrate!**

Yay! Congratulations on the first big two parts.

## **Parts Two Further Study**

There are several possible additional tasks here.

### **Make a Homepage**

Change the homepage to a page that shows the 5 most recent posts.

![Screen Shot 2023-05-08 at 3.01.22 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef04ec26-9fb2-4e60-b2f8-56443837d0de/Screen_Shot_2023-05-08_at_3.01.22_PM.png)

### **Show Friendly Date**

When listing the posts (on the post index page, the homepage, and the user detail page), show a friendly-looking version of the date, like “May 1, 2015, 10:30 AM”.

### **Using Flash Messages for Notifications**

Use the Flask “flash message” feature to notify about form errors/successful submissions.

### **Add a Custom “404 Error Page”**

Research how to make a custom page that appears when a 404 error happens in Flask. Make such a page.

### **Cascade Deletion of User**

If you try to delete a user that has posts, you’ll get an ***IntegrityError*** — PostgreSQL raises an error because that would leave posts without a valid ***user_id***.

When a user is deleted, the related posts should be deleted, too.

You can find help for this at [Cascades](https://docs.sqlalchemy.org/en/latest/orm/cascades.html)>`_

# Many to Many-Blogly

# **Blogly**

## **Part Three: Add M2M Relationship**

The last part will be to add a “tagging” feature.

### **Tag Model**

![Screen Shot 2023-05-08 at 3.03.13 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4b764dd-ee1f-450a-a913-e14353e18216/Screen_Shot_2023-05-08_at_3.03.13_PM.png)

The site will have a table of tags — there should be an SQLAlchemy model for this:

- ***id***
- ***name***, (unique!)

There should also be a model for ***PostTag***, which joins together a ***Post*** and a ***Tag***. It will have foreign keys for the both the ***post_id*** and ***tag_id***. Since we don’t want the same post to be tagged to the same tag more than once, we’ll want the combination of post + tag to be unique. It also makes sense that neither the ***post_id*** nor ***tag_id*** can be null. Therefore, we’ll use a “composite primary key” for this table— a primary key made of more than one field. You may have to do some research to learn how to do this in SQLAlchemy.

Add relationships so you can see the ***.tags*** for a post, and the ***.posts*** for a tag.

**STOP** and play around with this feature in ***IPython*** before continuing.

### **User Interface**

1. **Add Tag**

![Screen Shot 2023-05-08 at 3.04.45 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/adcb908c-31bc-469e-934a-f7df80b75dd2/Screen_Shot_2023-05-08_at_3.04.45_PM.png)

2. **Edit Tag**

![Screen Shot 2023-05-08 at 3.09.35 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41092caa-0fb7-43ff-a794-1a2be68296cf/Screen_Shot_2023-05-08_at_3.09.35_PM.png)

3. **List Tag**

![Screen Shot 2023-05-08 at 3.11.42 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c61055c9-d050-415a-88f2-f5fdfb644dd5/Screen_Shot_2023-05-08_at_3.11.42_PM.png)

4. **Show Tag**

![Screen Shot 2023-05-08 at 3.14.48 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/527c480e-63a4-4d62-a97a-25f278ad4d3d/Screen_Shot_2023-05-08_at_3.14.48_PM.png)

5.  **Show Post With Tags**
    
    ![Screen Shot 2023-05-08 at 3.13.19 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e236b58b-1650-480d-98a7-9b276a634347/Screen_Shot_2023-05-08_at_3.13.19_PM.png)
    
6. **Add Post With Tags**

![Screen Shot 2023-05-08 at 3.16.01 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/82c29a03-c0f8-4e9f-b985-749ab10a571d/Screen_Shot_2023-05-08_at_3.16.01_PM.png)

7. **Edit Post With Tags**

![Screen Shot 2023-05-08 at 3.17.48 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ed79536-7149-430c-85e8-ef1a220484da/Screen_Shot_2023-05-08_at_3.17.48_PM.png)

### **Add Routes**

**GET */tags :*** Lists all tags, with links to the tag detail page.

**GET */tags/[tag-id] :*** Show detail about a tag. Have links to edit form and to delete.

**GET */tags/new :*** Shows a form to add a new tag.

**POST */tags/new :*** Process add form, adds tag, and redirect to tag list.

**GET */tags/[tag-id]/edit :*** Show edit form for a tag.

**POST */tags/[tag-id]/edit :*** Process edit form, edit tag, and redirects to the tags list.

**POST */tags/[tag-id]/delete :*** Delete a tag.

### **Update Routes for Posts**

Update the route that shows a post so that it shows all the tags for that post.

Update the routes for adding/editing posts so that it shows a listing of the tags and lets you pick which tag(s) apply to that post. (You can use whatever form element you want here: a multi-select, a list of checkboxes, or any other way you can solve this.

<aside>
💡 **Hint:** The normal way to get a value from a form, `request.form['key']`, only returns *one* value from this form. To get all of the values for that key in the form, you’ll want to investigate ***.getlist***.

</aside>

## **Further Study**

### **Update Tag Add/Edit Forms**

Edit these forms to let you pick posts for this tag.

1. **Edit Tag With Posts**

![Screen Shot 2023-05-08 at 3.19.18 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a210fe9-2725-439b-a68e-0e8cccf8faab/Screen_Shot_2023-05-08_at_3.19.18_PM.png)

2. If you made a homepage, make this show tags, too:

![Screen Shot 2023-05-08 at 3.21.10 PM.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b925b395-caac-44ef-8d53-180452246829/Screen_Shot_2023-05-08_at_3.21.10_PM.png)
