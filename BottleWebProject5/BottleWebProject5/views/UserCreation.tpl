% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>


<div class="wrapper">
  <form class="form-group" method='post' action='/createuser'>       
    <h2 class="form-group-heading">Create New User</h2>
    <input type="text" class="form-control" name="username" placeholder="Username" required="" autofocus="" />
    <input type="password" class="form-control" name="password" placeholder="Password" required=""/>
    <button class="btn btn-lg btn-primary btn-block" type="submit">Create User</button>   
  </form>
</div>


