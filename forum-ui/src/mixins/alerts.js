import { useSwal } from '@/plugins/swal';

export default function () {
  const Swal = useSwal()

  const alertSuccess = function () {
    // Use sweetalert2
    Swal.fire({
      position: "top-end",
      icon: "success",
      title: "Saved new Record",
      showConfirmButton: false,
      timer: 1000,
    })
  }

  const alertFailure = function () {
    Swal.fire({
      position: "top-end",
      icon: "error",
      title: "Request failed! Please try again!",
      showConfirmButton: false,
      timer: 1000,
    });
  }

  return {
    alertSuccess,
    alertFailure
  }
}
