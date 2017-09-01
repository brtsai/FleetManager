import { Component, OnInit } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {

    constructor(router : Router) {
        router.events.subscribe(s => {
          if (s instanceof NavigationEnd) {
            const tree = router.parseUrl(router.url);
            if (tree.fragment) {
              const element = document.querySelector("#" + tree.fragment);
              if (element) { element.scrollIntoView(element); }
            }
          }
        });
    }

    ngOnInit() {

    }

}
