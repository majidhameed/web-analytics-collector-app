% include('header.tpl', title='Login')
    <div class="container">
      <form method="post" action="/login" class="form-signin" role="form">
        <h2 class="form-signin-heading">Admin Login</h2>
        <input type="login" name="login" id="login" class="form-control" placeholder="Login" required autofocus>
        <input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
        <input type="submit" class="btn btn-lg btn-primary btn-block" type="submit" value="Sign in"/>
      </form>
    </div>
% include('footer.tpl')