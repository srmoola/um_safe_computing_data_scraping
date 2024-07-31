export const requestConvo = () => {
  const url =
    "https://umgpt.umich.edu/maizey/api/projects/96c3a60b-31ef-44ef-99f7-90253752a1f0/conversation/";
  const headers = {
    accept: "application/json",
    Authorization:
      "Bearer e5090cbeed6f10ca7d5d009d76c81deb0caa68a4c348e1acc63d709b9f91639a",
    "Content-Type": "application/json",
    "X-CSRFTOKEN":
      "1DHYqjRK7Zfy7CmwdPe8uggS6faYRFADbt4kihqS1jsegYVukyxrnInsOa36wIUo",
  };

  fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
};
