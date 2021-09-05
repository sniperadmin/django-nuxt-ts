export default function({ $auth, route, redirect }) {
  console.log($auth.loggedIn);
  if ($auth.loggedIn && (route.path === '/auth/login') || (route.path === '/auth/register')) {
    redirect('/')
  }
}
