import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LecNavBarComponent } from './lec-nav-bar.component';

describe('LecNavBarComponent', () => {
  let component: LecNavBarComponent;
  let fixture: ComponentFixture<LecNavBarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LecNavBarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LecNavBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
