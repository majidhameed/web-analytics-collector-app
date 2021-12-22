% include('header.tpl', title="Admin Home")
  <!-- MENU -->
  <div class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Admin Home</a>
    </div>
    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li><a href="/tracking_code">tracking code</a></li>
        <li><a href="/accounts">accounts</a></li>
        <li><a href="/cleanup">cleanup</a></li>
  		<li><a href="/referals">referals</a></li>
  		<li><a href="/referals_url">referals - by url</a></li>
	  	<li><a href="/referals_ip">referals - by IP</a></li>
	  	<li><a href="/users_ip">users by ip</a></li>
	  	<li><a href="/new_ips">new ips</a></li>
	  	<li><a href="/category_breakdown">category breakdown</a></li>
	  	<li><a href="/potential_breakdown">potential breakdown</a></li>
	  	<li><a href="/potential_breakdown">potential breakdown</a></li>
	  	<li><a href="/url_tagging">url tagging</a></li>
	   </ul>
    </div><!--/.nav-collapse -->
  </div>
</div><!--/.navbar -->
% include('footer.tpl')