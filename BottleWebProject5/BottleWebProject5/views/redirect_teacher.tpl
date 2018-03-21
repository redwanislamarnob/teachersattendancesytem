% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<p> {{ username }} has logged in from {{ IP }} </p> 

<table class="table table-hover">
  <thead>
    <tr>
      <th>Login Date</th>
      <th>Login Time</th>
	  <th>Login IP</th>
    </tr>
  </thead>
  <tbody>
	% for elem in object['logindetails'] :
	<tr> 
		<td> {{ elem['logindate'] }} </td>
		<td> {{ elem['logintime'] }} </td>
		<td> {{ elem['loginip'] }} </td>
	</tr>
	% end
  </tbody>
</table>



