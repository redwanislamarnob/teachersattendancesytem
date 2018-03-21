% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<a type="button" class="btn btn-primary" href="/redirect_to_create"> Create User </a>

<div class="list-group">
% for teacher in collection.find({'usertype':'teacher'}) : 
<a class="list-group-item" data-toggle="collapse" href="#{{ teacher['username'] }}"> {{teacher['username']}} </a>
<div class="collapse" id="{{ teacher['username'] }}">
	<table class="table table-hover">
  <thead>
    <tr>
      <th>Login Date</th>
      <th>Login Time</th>
	  <th>Login IP</th>
    </tr>
  </thead>
  <tbody>
	% for elem in teacher['logindetails'] :
	<tr> 
		<td> {{ elem['logindate'] }} </td>
		<td> {{ elem['logintime'] }} </td>
		<td> {{ elem['loginip'] }} </td>
	</tr>
	% end
  </tbody>
</table>
</div>
% end
</div>

